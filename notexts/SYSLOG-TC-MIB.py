#
# PySNMP MIB module SYSLOG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SYSLOG-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 19:25:34 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, MibIdentifier, NotificationType, Gauge32, mib_2, TimeTicks, ObjectIdentity, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "mib-2", "TimeTicks", "ObjectIdentity", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
syslogTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 173))
syslogTCMIB.setRevisions(('2009-03-30 00:00',))
if mibBuilder.loadTexts: syslogTCMIB.setLastUpdated('200903300000Z')
if mibBuilder.loadTexts: syslogTCMIB.setOrganization('IETF Syslog Working Group')
class SyslogFacility(TextualConvention, Integer32):
    reference = 'The Syslog Protocol (RFC5424): Table 1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kern", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), ("authpriv", 10), ("ftp", 11), ("ntp", 12), ("audit", 13), ("console", 14), ("cron2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class SyslogSeverity(TextualConvention, Integer32):
    reference = 'The Syslog Protocol (RFC5424): Table 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emerg", 0), ("alert", 1), ("crit", 2), ("err", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

mibBuilder.exportSymbols("SYSLOG-TC-MIB", PYSNMP_MODULE_ID=syslogTCMIB, syslogTCMIB=syslogTCMIB, SyslogSeverity=SyslogSeverity, SyslogFacility=SyslogFacility)
