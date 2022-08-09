#
# PySNMP MIB module PACKETLOGIC-HW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:50:39 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, iso, ObjectIdentity, IpAddress, Unsigned32, Counter32, TimeTicks, MibIdentifier, Gauge32, Bits, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Unsigned32", "Counter32", "TimeTicks", "MibIdentifier", "Gauge32", "Bits", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
hw = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30))
hw.setRevisions(('2019-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hw.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: hw.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: hw.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: hw.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: hw.setDescription('MIB for PacketLogic2 Hardware')
mibBuilder.exportSymbols("PACKETLOGIC-HW-MIB", hw=hw, PYSNMP_MODULE_ID=hw)
