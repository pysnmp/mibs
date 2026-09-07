#
# PySNMP MIB module CISCO-REPORT-INTERVAL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-REPORT-INTERVAL-TC-MIB
# Source digest sha256:03e9ca190a3cbc95faa263adea623c4725abb74d37117fee22753fbfcdea3792
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoReportIntervalTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 670))
ciscoReportIntervalTcMIB.setRevisions(('2008-08-22 00:00',))
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setLastUpdated('2008-08-22 00:00')
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setOrganization('Cisco Systems, Inc.')
class ReportCurrentCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

class ReportIntervalCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("CISCO-REPORT-INTERVAL-TC-MIB", PYSNMP_MODULE_ID=ciscoReportIntervalTcMIB, ReportCurrentCount=ReportCurrentCount, ReportIntervalCount=ReportIntervalCount, ciscoReportIntervalTcMIB=ciscoReportIntervalTcMIB)
