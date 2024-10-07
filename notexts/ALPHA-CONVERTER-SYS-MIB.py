#
# PySNMP MIB module ALPHA-CONVERTER-SYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alpha/ALPHA-CONVERTER-SYS-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:49:47 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
simple, ScaledNumber = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "simple", "ScaledNumber")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, Counter32, Unsigned32, Integer32, iso, ModuleIdentity, ObjectIdentity, IpAddress, Gauge32, Counter64, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "Counter32", "Unsigned32", "Integer32", "iso", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
converterSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2))
converterSystem.setRevisions(('2015-07-28 00:00', '2015-07-23 00:00', '2015-06-23 00:00',))
if mibBuilder.loadTexts: converterSystem.setLastUpdated('201507280000Z')
if mibBuilder.loadTexts: converterSystem.setOrganization('Alpha Technologies Ltd.')
convSysTotalOutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 1), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalOutputCurrent.setStatus('current')
convSysTotalOutputPower = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 2), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalOutputPower.setStatus('current')
convSysTotalCapacityInstalledAmps = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 3), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalCapacityInstalledAmps.setStatus('current')
convSysTotalCapacityInstalledPower = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 4), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalCapacityInstalledPower.setStatus('current')
convSysAverageConverterOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 5), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysAverageConverterOutputVoltage.setStatus('current')
convSysAverageConverterInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 6), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysAverageConverterInputVoltage.setStatus('current')
convSysSystemVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 7), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysSystemVoltage.setStatus('current')
convSysTotalLoadCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 8), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalLoadCurrent.setStatus('current')
convSysSystemNumber = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 9), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysSystemNumber.setStatus('current')
conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100))
compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 1))
compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 1, 1)).setObjects(("ALPHA-CONVERTER-SYS-MIB", "converterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    compliance = compliance.setStatus('current')
converterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 2))
converterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 2, 1)).setObjects(("ALPHA-CONVERTER-SYS-MIB", "convSysTotalOutputCurrent"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalOutputPower"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalCapacityInstalledAmps"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalCapacityInstalledPower"), ("ALPHA-CONVERTER-SYS-MIB", "convSysAverageConverterOutputVoltage"), ("ALPHA-CONVERTER-SYS-MIB", "convSysAverageConverterInputVoltage"), ("ALPHA-CONVERTER-SYS-MIB", "convSysSystemVoltage"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalLoadCurrent"), ("ALPHA-CONVERTER-SYS-MIB", "convSysSystemNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    converterGroup = converterGroup.setStatus('current')
mibBuilder.exportSymbols("ALPHA-CONVERTER-SYS-MIB", converterSystem=converterSystem, convSysTotalOutputCurrent=convSysTotalOutputCurrent, convSysTotalCapacityInstalledPower=convSysTotalCapacityInstalledPower, convSysTotalLoadCurrent=convSysTotalLoadCurrent, convSysTotalOutputPower=convSysTotalOutputPower, converterGroups=converterGroups, converterGroup=converterGroup, convSysAverageConverterInputVoltage=convSysAverageConverterInputVoltage, convSysSystemNumber=convSysSystemNumber, compliances=compliances, convSysSystemVoltage=convSysSystemVoltage, convSysAverageConverterOutputVoltage=convSysAverageConverterOutputVoltage, convSysTotalCapacityInstalledAmps=convSysTotalCapacityInstalledAmps, conformance=conformance, compliance=compliance, PYSNMP_MODULE_ID=converterSystem)
