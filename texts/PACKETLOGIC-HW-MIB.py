#
# PySNMP MIB module PACKETLOGIC-HW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-HW-MIB
# Produced by pysmi-1.1.12 at Wed Nov  6 08:34:48 2024
# On host fv-az984-999 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, ModuleIdentity, Unsigned32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter32, IpAddress, ObjectIdentity, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter32", "IpAddress", "ObjectIdentity", "Counter64", "TimeTicks")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
hw = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 30))
hw.setRevisions(('2019-09-12 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hw.setRevisionsDescriptions((' Latest version at the revision date for version GET VERSION HERE',))
if mibBuilder.loadTexts: hw.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: hw.setOrganization('Procera Networks, Inc.')
if mibBuilder.loadTexts: hw.setContactInfo('support@proceranetworks.com')
if mibBuilder.loadTexts: hw.setDescription('MIB for PacketLogic2 Hardware')
mibBuilder.exportSymbols("PACKETLOGIC-HW-MIB", hw=hw, PYSNMP_MODULE_ID=hw)
