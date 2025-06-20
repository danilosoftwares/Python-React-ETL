import React, { useEffect, useRef, useState } from 'react';
import { ProgressSpinner } from 'primereact/progressspinner';
import { fetchJob } from '../../services/jobService';

interface ProgressingProps {
    jobId: string | undefined;
    onFinish: Function;
}

export const Progressing: React.FC<ProgressingProps> = ({ jobId, onFinish }) => {
    const [percent, setPecent] = useState(0);
    const intervalRef = useRef<NodeJS.Timeout | null>(null);

    const progressMessages = [
        { min: 90, message: "Finalizing things with care — hang in there!" },
        { min: 60, message: "Just a bit more and everything will be in place." },
        { min: 45, message: "You’re doing great. We’ll be ready in just a moment!" },
        { min: 25, message: "Thanks for your patience — we’re almost done!" },
        { min: 0, message: "No worries, we’re taking care of everything!" },
    ];

    const getProgressMessage = (percent: number) => {
        const found = progressMessages.find(({ min }) => percent > min);
        return found?.message ?? "";
    };

    const closeTimer = () => {
        clearInterval(intervalRef.current!);
        setPecent(0);
        onFinish();
    }

    useEffect(() => {
        if (jobId) {
            intervalRef.current = setInterval(async () => {
                try {
                    const response = await fetchJob(jobId);
                    setPecent(response.percent);
                    if (response.percent === 100) {
                        closeTimer();
                    }
                } catch (error) {
                    closeTimer();
                }
            }, 2000);
        }
    // eslint-disable-next-line
    }, [jobId]);

    return (
        <div style={{ display: 'flex', flexDirection: 'column', margin: '10px 10%', height: '96vh', justifyContent: 'center' }}>
            <h3>{getProgressMessage(percent)}</h3>
            {percent === 0 ? <ProgressSpinner /> : <div style={{ width: "100%", height: "8px", background: "#e5e7eb", borderRadius: "8px" }}><div style={{ width: percent.toString() + "%", backgroundColor: "#2563eb", height: "100%", borderRadius: "8px" }}></div></div>}
        </div>
    );
};

