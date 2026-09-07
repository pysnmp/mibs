#
# PySNMP MIB module PCUBE-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source PCUBE-CONFIG-COPY-MIB
# Source digest sha256:2c7fde57c15262b2edf8211b0c7ed7d340663d7ef7b5e6024d96901644eed350
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
pcubeMgmt, = mibBuilder.importSymbols("PCUBE-SMI", "pcubeMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
pcubeConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5655, 3, 1))
pcubeConfigCopyMIB.setRevisions(('2006-04-06 20:00', '2002-01-14 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pcubeConfigCopyMIB.setRevisionsDescriptions(('The original mib has been chagned to use SMIv2 syntax.\n         Clarified descriptions in the mib.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setLastUpdated('2006-04-06 20:00')
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setContactInfo('Cisco Systems\n                  Customer Service\n                  \n           Postal: 170 W Tasman Drive\n                   San Jose, CA  95134\n                   USA\n\n              Tel: +1 800 553-NETS\n\n           E-mail: cs-sce@cisco.com')
if mibBuilder.loadTexts: pcubeConfigCopyMIB.setDescription("This MIB facilitates writing of  running\n         configuration of the SCOS to \n         startup configuration.\n         A config-copy operation is a request to \n         copy a configuration file of a running \n         SCOS. The term 'agent-config' will \n         be used in this MIB to refer to either\n         the running config or the startup config.\n         The term SCE refers to Service Control Engine")
class ConfigFileType(TextualConvention, Integer32):
    description = 'The various types of files on which a config-copy\n        operation can be performed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("startupConfig", 1), ("runningConfig", 2))

pcubeConfigCopyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1))
pcubeConfigCopyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2))
pcubeConfigCopyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1))
pcubeConfigCopyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2))
pcubeCopy = MibIdentifier((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1))
pcubeCopyTable = MibTable((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: pcubeCopyTable.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyTable.setDescription('A table of config-copy requests.')
pcubeCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "PCUBE-CONFIG-COPY-MIB", "pcubeCopyIndex"))
if mibBuilder.loadTexts: pcubeCopyEntry.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyEntry.setDescription("A config-copy request.\n\n        A management station wishing to save the running config\n        may use any number to be used as an index.\n        The station should then create the associated instance of the \n        row status and row index objects.  \n        It should be noted however that currently \n        'pcubeCopySourceFileType' must be of 'runningConfig' type and \n        'pcubeCopyDestFileType' must be of 'startupConfig' type \n        (that are the default values).\n        \n        After setting pcubeCopySourceFileType and pcubeCopyDestFileType\n        objects by explicit SNMP request or or by default, the row status\n        should be set to createAndGo to initiate the request. \n        Note that this entire procedure may be initiated \n        via a single set request which specifies a row \n        status of 'createAndGo(4)'.")
pcubeCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: pcubeCopyIndex.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyIndex.setDescription("Object which specifies a unique entry in the\n        pcubeCopyTable.  A management station wishing\n        to initiate a config-copy operation should use a\n        random value for this object when creating\n        or modifying an instance of a 'pcubeCopyEntry'.\n        The RowStatus semantics of the 'pcubeCopyEntryRowStatus'\n        object will prevent access conflicts.")
pcubeCopyEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopyEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyEntryRowStatus.setDescription('This object can be used for creating/deleting entries \n        from the table.')
pcubeCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 3), ConfigFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopySourceFileType.setStatus('current')
if mibBuilder.loadTexts: pcubeCopySourceFileType.setDescription("Specifies the type of file to copy from. \n        Currently only 'runningConfig(2)' is supported.")
pcubeCopyDestFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 5655, 3, 1, 1, 1, 1, 1, 4), ConfigFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pcubeCopyDestFileType.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyDestFileType.setDescription("Specifies the type of file to copy to.\n        currently only 'startupConfig(1)' is supported.")
pcubeConfigCopyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 2, 1)).setObjects(("PCUBE-CONFIG-COPY-MIB", "pcubeCopyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeConfigCopyMIBCompliance = pcubeConfigCopyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: pcubeConfigCopyMIBCompliance.setDescription('A compliance statement defined in this MIB module,\n         for SCE SNMP agents.')
pcubeCopyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5655, 3, 1, 2, 1, 1)).setObjects(("PCUBE-CONFIG-COPY-MIB", "pcubeCopyEntryRowStatus"), ("PCUBE-CONFIG-COPY-MIB", "pcubeCopySourceFileType"), ("PCUBE-CONFIG-COPY-MIB", "pcubeCopyDestFileType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pcubeCopyGroup = pcubeCopyGroup.setStatus('current')
if mibBuilder.loadTexts: pcubeCopyGroup.setDescription('A collection of objects used for specifying \n                            the configuration of the copy operation.')
mibBuilder.exportSymbols("PCUBE-CONFIG-COPY-MIB", ConfigFileType=ConfigFileType, PYSNMP_MODULE_ID=pcubeConfigCopyMIB, pcubeConfigCopyMIB=pcubeConfigCopyMIB, pcubeConfigCopyMIBCompliance=pcubeConfigCopyMIBCompliance, pcubeConfigCopyMIBCompliances=pcubeConfigCopyMIBCompliances, pcubeConfigCopyMIBConformance=pcubeConfigCopyMIBConformance, pcubeConfigCopyMIBGroups=pcubeConfigCopyMIBGroups, pcubeConfigCopyMIBObjects=pcubeConfigCopyMIBObjects, pcubeCopy=pcubeCopy, pcubeCopyDestFileType=pcubeCopyDestFileType, pcubeCopyEntry=pcubeCopyEntry, pcubeCopyEntryRowStatus=pcubeCopyEntryRowStatus, pcubeCopyGroup=pcubeCopyGroup, pcubeCopyIndex=pcubeCopyIndex, pcubeCopySourceFileType=pcubeCopySourceFileType, pcubeCopyTable=pcubeCopyTable)
